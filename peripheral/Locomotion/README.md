# Locomotion

Controls the main left and right motors on R2.

## Properties

| Type | Request | Response |
| :---: | :--- | :--- |
| LM | 1 byte direction, 1 byte speed (0 to 255, 50 deadzone) | None |
| RM | 1 byte direction, 1 byte speed (0 to 255, 50 deadzone) | None |
| BM | LM then RM | None |
| STOP | None | None |
