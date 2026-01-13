# Computer Shop Django Project

A full-featured e-commerce website for selling computers built with Django.

## Features

- **Admin Panel**: Manage categories, products, and orders
- **Product Catalog**: Browse and filter products by category
- **Shopping Cart**: Add/remove items, update quantities
- **Checkout Process**: Complete order with customer information
- **Order Management**: Track order status (Pending, Confirmed, Delivered)

## Project Structure

```
computershop/
├── computershop/          # Main project settings
├── store/                 # Store app
│   ├── models.py         # Category, Product, Order, OrderItem models
│   ├── views.py          # All view functions
│   ├── urls.py           # Store app URLs
│   ├── admin.py          # Admin panel configuration
│   └── templates/store/  # HTML templates
├── media/                 # Upload directory for product images
└── requirements.txt       # Project dependencies
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser
```bash
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

## URLs

- `/` - Home page (product list)
- `/product/<id>/` - Product detail page
- `/cart/` - Shopping cart
- `/checkout/` - Checkout form
- `/success/` - Order success page
- `/admin/` - Admin panel

## Admin Panel Features

- **Categories**: Add/edit/delete product categories
- **Products**: Add/edit/delete products with images and stock management
- **Orders**: View all orders, update order status, see order details
- **Order Items**: View individual order items

## Cart Functionality

- Uses Django sessions to store cart data
- Stores product ID and quantity for each item
- Calculates total price automatically
- Supports adding, updating, and removing items

## Technical Details

- **Framework**: Django 5.2.4
- **Database**: SQLite (development)
- **Image Handling**: Pillow for ImageField support
- **Frontend**: Django templates with inline CSS
- **No JavaScript frameworks** - pure Django and HTML/CSS

## Getting Started

1. Follow the setup instructions above
2. Create a superuser to access the admin panel
3. Add some categories and products through the admin panel
4. Browse the shop at `http://127.0.0.1:8000/`
5. Test the complete shopping flow from browsing to checkout

## Notes

- Product images should be uploaded through the admin panel
- The media directory is automatically created for image uploads
- All styling is done with inline CSS for simplicity
- The project uses function-based views as requested
