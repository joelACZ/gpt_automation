# utils/selectors.py

# Definición centralizada de selectores (IDs, clases, XPaths)
# Facilita mantenimiento y evita hardcodeo en múltiples módulos


class Selectores:
    # Login email page
    EMAIL_INPUT_ID = "username"
    PASSWORD_INPUT_ID = "password"

    # ChatGPT main interface
    # Área de texto para enviar prompts
    CHAT_TEXTAREA_TAG = "textarea"
    # Clase de los bloques de respuesta en Markdown
    RESPONSE_MARKDOWN_CLASS = "markdown"
    # Clase que indica que el modelo está escribiendo
    TYPING_INDICATOR_CLASS = "typing"

    # URLs
    LOGIN_URL = "https://chat.openai.com/auth/login"
    CHAT_URL = "https://chat.openai.com/chat"

    # XPaths u otros selectores opcionales
    # Ejemplo: botón de enviar si cambia el TAG
    # SEND_BUTTON_XPATH = "//button[@aria-label='Enviar']"


# Uso:
# from utils.selectors import Selectores
# driver.find_element(By.ID, Selectores.EMAIL_INPUT_ID)
