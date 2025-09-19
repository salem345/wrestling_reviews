# PythonAnywhere Deployment Steps

## 🚀 Step 1: Upload Files to PythonAnywhere

### Option A: Using Git (Recommended)
```bash
# Navigate to your project directory
cd ~/wrestling_reviews

# If you haven't initialized git yet:
git init
git remote add origin https://github.com/salem345/wrestling_reviews.git

# Pull the latest changes
git pull origin main

# Or if you have local changes, stash them first:
git stash
git pull origin main
git stash pop
```

### Option B: Manual File Upload
1. Go to PythonAnywhere Files tab
2. Navigate to `/home/salem2026/wrestling_reviews/`
3. Upload the modified files manually

## 🔧 Step 2: Update Your Files via Bash Console

Open a **Bash console** on PythonAnywhere and run:

```bash
# Navigate to your project
cd ~/wrestling_reviews

# Create the templates directory structure if it doesn't exist
mkdir -p templates/events
mkdir -p templates/wrestlers  
mkdir -p templates/reviews
mkdir -p templates/registration
mkdir -p static/css

# Make sure you have the correct file structure
ls -la templates/
```

## 📁 Step 3: Verify File Structure

Your directory should look like this:
```
wrestling_reviews/
├── wrestling_reviews/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── events/
│   │   ├── list.html
│   │   ├── detail.html
│   │   ├── form.html
│   │   └── confirm_delete.html
│   ├── wrestlers/
│   │   ├── list.html
│   │   ├── detail.html
│   │   ├── form.html
│   │   └── confirm_delete.html
│   ├── reviews/
│   │   ├── list.html
│   │   ├── detail.html
│   │   ├── form.html
│   │   └── confirm_delete.html
│   └── registration/
│       └── login.html
├── static/
│   └── css/
│       └── style.css
├── manage.py
└── requirements.txt
```

## 🗄️ Step 4: Database Migrations

```bash
# Navigate to your project
cd ~/wrestling_reviews

# Run migrations to update database structure
python3.10 manage.py makemigrations
python3.10 manage.py migrate

# Create superuser if you haven't already
python3.10 manage.py createsuperuser
# Follow prompts to create your admin account
```

## 📦 Step 5: Collect Static Files

```bash
# Collect all static files
python3.10 manage.py collectstatic --noinput
```

## 🔄 Step 6: Restart Your Web App

1. Go to PythonAnywhere **Web** tab
2. Find your web app (salem2026.pythonanywhere.com)
3. Click the **"Reload"** button
4. Wait for the green checkmark

## ✅ Step 7: Test Your Site

Visit your site and test:
1. **Homepage**: Should load with new design
2. **Login**: Go to `/login/` and login with your superuser account
3. **Admin Functions**: You should see "Admin" menu in navbar
4. **Add Review**: Test adding a review (should work now)
5. **Delete Functions**: Try deleting an event or wrestler

## 🐛 Step 8: Troubleshooting

If you encounter issues:

### Check Error Logs
```bash
# View recent error logs
tail -f ~/logs/error.log
tail -f ~/logs/access.log
```

### Check Django Settings
```bash
cd ~/wrestling_reviews
python3.10 manage.py check
```

### Test Database Connection
```bash
python3.10 manage.py shell
```
Then in Python shell:
```python
from users.models import User
print(User.objects.count())
exit()
```

### Fix Static Files Issues
```bash
# If static files aren't loading
python3.10 manage.py collectstatic --clear --noinput
```

## 🔐 Step 9: Security Check

Make sure your settings are correct:
```bash
cd ~/wrestling_reviews
python3.10 manage.py check --deploy
```

## 📝 Step 10: Final Verification

Test these URLs on your live site:
- `https://salem2026.pythonanywhere.com/` - Homepage
- `https://salem2026.pythonanywhere.com/login/` - Login page
- `https://salem2026.pythonanywhere.com/reviews/` - Reviews list
- `https://salem2026.pythonanywhere.com/events/` - Events list
- `https://salem2026.pythonanywhere.com/wrestlers/` - Wrestlers list

## 🎉 You're Done!

Your site should now have:
- ✅ Professional design
- ✅ Delete functionality for events
- ✅ Superuser-only access for admin functions
- ✅ Working review system
- ✅ Login/logout functionality

If you encounter any issues, check the error logs and let me know!