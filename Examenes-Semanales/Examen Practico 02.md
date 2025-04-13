
# `02` Examen Practico
**Objetivo**: Crear un sistema que permita controlar funciones de un reproductor multimedia usando gestos con la mano.  
**Requiere integración con:**
- MediaPipe Hands
- Lógica condicional personalizada
- PyAutoGUI o similar para controlar el sistema

```
Diseña un sistema que reconozca al menos 4 gestos:
- ✋ Mano abierta → Pausar/reanudar música
- 👍 Pulgar arriba → Subir volumen
- 👎 Pulgar abajo → Bajar volumen
- 👉 Dedo índice apuntando → Siguiente canción

Al detectar cada gesto, usa PyAutoGUI para simular una tecla (ej. space, volumen arriba/abajo, etc.). Debes manejar falsos positivos y evitar que el mismo gesto se detecte múltiples veces seguidas. Implementa un delay o cooldown de detección.
```
