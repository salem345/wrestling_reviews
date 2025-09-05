# Wrestling Reviews - PythonAnywhere Deployment Guide

## Prerequisites
1. PythonAnywhere account (free or paid)
2. Your project files uploaded to PythonAnywhere

## Step-by-Step Deployment

### 1. Upload Your Project
- Upload all your project files to `/home/yourusername/wrestling_reviews/`
- Make sure all files are in the correct directory structure

### 2. Install Dependencies
Open a Bash console in PythonAnywhere and run:
```bash
cd ~/wrestling_reviews
pip3.10 install --user -r requirements.txt
```

### 3. Database Setup
```bash
cd ~/wrestling_reviews
python3.10 manage.py makemigrations
python3.10 manage.py migrate
python3.10 manage.py collectstatic --noinput
```

### 4. Create Superuser (Optional)
```bash
python3.10 manage.py createsuperuser
```

### 5. Configure Web App
1. Go to the "Web" tab in your PythonAnywhere dashboard
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Set the source code directory to: `/home/yourusername/wrestling_reviews`
6. Set the working directory to: `/home/yourusername/wrestling_reviews`

### 6. Configure WSGI File
1. Click on the WSGI configuration file link
2. Replace the contents with the code from `pythonanywhere_wsgi.py`
3. Update `yourusername` with your actual PythonAnywhere username

### 7. Static Files Configuration
In the "Web" tab, add a static files mapping:
- URL: `/static/`
- Directory: `/home/yourusername/wrestling_reviews/staticfiles/`

### 8. Update Settings for Production
Add to your `settings.py`:
```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'localhost', '127.0.0.1']

# Static files settings
STATIC_ROOT = '/home/yourusername/wrestling_reviews/staticfiles'
```

### 9. Reload Your Web App
Click the "Reload" button in the Web tab.

## Testing Your Deployment

1. Visit `https://yourusername.pythonanywhere.com`
2. Test all functionality:
   - View reviews, wrestlers, and events
   - Add new reviews
   - Edit existing content
   - Search and filter features

## Troubleshooting

### Common Issues:
1. **Static files not loading**: Make sure `collectstatic` was run and static files mapping is correct
2. **Database errors**: Ensure migrations were run properly
3. **Import errors**: Check that all dependencies are installed with `--user` flag

### Logs:
Check error logs in the Web tab if something isn't working.

## Features Included

✅ **Complete Web Interface**
- Modern, responsive design with Bootstrap 5
- Professional wrestling-themed styling
- Mobile-friendly layout

✅ **Full CRUD Operations**
- Add, edit, delete reviews
- Manage wrestlers and events
- User-friendly forms with validation

✅ **Advanced Features**
- Search functionality across all content
- Filter reviews by rating
- Filter events by promotion
- Pagination for large datasets
- Star rating display system

✅ **Professional Design**
- Clean, modern interface
- Intuitive navigation
- Consistent styling throughout
- Interactive elements with hover effects

## API Endpoints (Still Available)
Your existing API endpoints remain functional:
- `/api/reviews/` - Reviews API
- `/api/wrestlers/` - Wrestlers API  
- `/api/events/` - Events API
- `/api/users/` - Users API

## Next Steps
1. Add some sample data through the admin panel or web interface
2. Test all functionality thoroughly
3. Consider adding user authentication for production use
4. Customize the design further if needed

Your wrestling reviews project is now ready for production use on PythonAnywhere!