from plyer import notification

notification.notify(
    title='¡Aviso!',
    message='Tu programa ha terminado correctamente.',
    app_name='Mi Aplicación',
    timeout=5  # segundos que dura la notificación
)