source /SISTEMA-ESTOQUE/venv/Scripts/activate

# Rodar as migrações e iniciar o servidor
python manage.py migrate
python manage.py runserver 0.0.0.0:$PORT