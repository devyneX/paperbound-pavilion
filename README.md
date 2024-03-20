
## Dev

### Prerequisites
1. Python
2. Docker 
3. Poetry
3. Node

### Get Started
- Clone
```bash
git clone https://github.com/devyneX/paperbound-pavilion.git
```
- Run db and redis
```bash
make run-dependencies
```
- Update 
```bash
make update
```
- Install frontend dependencies
```bash
npm install
```
- Run this in the terminal 
```bash
npm run tailwind
```
 while you do development to compile TailwindCSS on demand.
- Run server
```bash
make run-server
```

- Run Celery worker
```bash
make run-celery
```

### Get updates 
- Pull
- Run `make update`

### Linting
- Run `make lint`

### Adding Packages
To add python package with poetry
```bash
make add-lib package_name
```

To add dev python package with poetry
```bash
make add-lib-dev package_name
```

### Code Guidelines
- Inherit models from `src.core.models.BaseModel`
- Templates to be extend from 
  - `src/core/templates/_base.html`
    - base template without navbar
  - `src/core/templates/base.html`
    - base template with navbar
  - `src/store_admin/templates/admin_base.html`
    - admin base template 
- Templates to include 
  - `src/core/templates/_form.html`
    - prebuilt form 
    - include as `{% include '_form.py' with submit_text="your-custom-submit-text" %}`
  - `src/core/templates/form.html`
    - prebuilt form with form_title
    - include as `{% include 'form.py' with form_title="your-custom-form-title" submit_text="your-custom-submit-text" %}`

### Contributing
- Create a new branch
- Make changes
- Push changes
- Create a PR