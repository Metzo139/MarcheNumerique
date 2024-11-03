from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Modèle utilisateur personnalisé
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('agriculteur', 'Agriculteur'),
        ('operateur', 'Opérateur'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    # Ajout de related_name pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Changez ce nom selon votre préférence
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Changez ce nom selon votre préférence
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
)
# Modèle Agriculteur
class Agriculteur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

# Modèle Opérateur
class Operateur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

# Modèle Produit
class Produit(models.Model):
    agriculteur = models.ForeignKey(Agriculteur, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

# Modèle Commande
class Commande(models.Model):
    operateur = models.ForeignKey(Operateur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('pending', 'En attente'), ('completed', 'Complétée')])
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande {self.id} - {self.produit.name}"

# Modèle Transaction
class Transaction(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.amount} FCFA"

# Modèle Feedback
class Feedback(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()  # Échelle de 1 à 5 par exemple
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Feedback pour {self.produit.name} - {self.rating} étoiles"

# Modèle Suivi de Stock
class SuiviDeStock(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    current_quantity = models.IntegerField()
    alert_threshold = models.IntegerField()

    def __str__(self):
        return f"Suivi de stock pour {self.produit.name}"