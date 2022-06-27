|**Nombre del Use Case**:   |**ID**: 41  |

|Nombre del CU: Cancelar reserva | ID: 41|
|---------------------------|--------------------|
|**Actor Principal**: Huesped |**Actor Secundario**: no aplica|
|**Tipo de Use Case**:   Concreto  |
|**Objetivo**: Registrar la cancelación de la reserva por parte de la huésped con su motivo correspondiente.|
|**Precondiciones**:  Cuando un huésped desea cancelar una reserva, deberá acceder con su usuario y contraseña al sistema de información. (C.U. 28 ejecutado con éxito)|
|**Post-Condiciones**|**Éxito:** Se registró la cancelación de una reserva quedando la misma en estado “cancelada” y la cabaña asociada en estado “disponible”.| B

|**Fracaso:** El caso de uso se cancela cuando:*   La fecha actual es mayor a la fecha de inicio de hospedaje de la reserva en cuestión.*   El estado de la reserva seleccionada no es “confirmada”.|
