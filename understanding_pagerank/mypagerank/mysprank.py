from Sqlconnector import SQLiteConnector

my_sql_connector = SQLiteConnector()
my_connection = my_sql_connector.connect('oospider')
my_cursor = my_connection.cursor()

# Find the ids that send out page rank - we only are interested
# in pages in the SCC that have in and out links
my_cursor.execute('''SELECT DISTINCT from_id FROM Links''')
from_ids = list()
for link in my_cursor: 
    from_ids.append(link[0])

# print(from_ids)
# # Find the ids that receive page rank 
to_ids = list()
links = list()
my_cursor.execute('''SELECT DISTINCT from_id, to_id FROM Links''')

for link in my_cursor:
    from_id = link[0]
    to_id = link[1]
    if from_id == to_id : continue
    if from_id not in from_ids : continue 
    if to_id not in from_ids : continue
    links.append(link)
    if to_id not in to_ids : to_ids.append(to_id)

# # Get latest page ranks for strongly connected component
prev_ranks = dict()
for node in from_ids:
    my_cursor.execute('''SELECT new_rank FROM Pages WHERE id = ?''', (node, ))
    actual_rank = my_cursor.fetchone()
    prev_ranks[node] = actual_rank[0]

sval = input('How many iterations:')
many = 1
if ( len(sval) > 0 ) : many = int(sval)

# Sanity check
if len(prev_ranks) < 1 : 
    print("Nothing to page rank.  Check data.")
    quit()

# # Lets do Page Rank in memory so it is really fast
for i in range(many):
    next_ranks = dict();
    total = 0.0
    '''prev_ranks.items is already theorically a list of tuples but it really returns a dict_items object
    that's why chuck use the list() method'''
    for (node, old_rank) in list(prev_ranks.items()):
        total = total + old_rank
        next_ranks[node] = 0.0
    # print total

    # Find the number of outbound links and sent the page rank down each
    for (node, old_rank) in list(prev_ranks.items()):
#       # print node, old_rank
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != node : continue
           #  print '   ',from_id,to_id

            if to_id not in to_ids: continue
            give_ids.append(to_id)
        if ( len(give_ids) < 1 ) : continue
        amount = old_rank / len(give_ids)
        print('debug AMOUNT:',amount)
#         # print node, old_rank,amount, give_ids
    
        for id in give_ids:
            next_ranks[id] = next_ranks[id] + amount
    
    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank
    evap = (total - newtot) / len(next_ranks)

    # print newtot, evap
    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap

    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank

#     # Compute the per-page average change from old rank to new rank
#     # As indication of convergence of the algorithm
    '''THIS IS JUST FOR PRINTING'''
    totdiff = 0
    for (node, old_rank) in list(prev_ranks.items()):
        new_rank = next_ranks[node]
        diff = abs(old_rank-new_rank)
        totdiff = totdiff + diff

    avediff = totdiff / len(prev_ranks)
    print(i+1, avediff)

    # rotate
    prev_ranks = next_ranks

# # Put the final ranks back into the database
print(list(next_ranks.items())[:5])
my_cursor.execute('''UPDATE Pages SET old_rank=new_rank''')
for (id, new_rank) in list(next_ranks.items()) :
    my_cursor.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, id))
my_connection.commit()
my_cursor.close()

