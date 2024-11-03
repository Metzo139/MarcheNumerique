from django.contrib import admin
from .models import CustomUser, Agriculteur, Operateur, Produit, Commande, Transaction, Feedback, SuiviDeStock

# Enregistrement de CustomUser dans l'admin
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')
    list_filter = ('user_type',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Enregistrement des autres modèles
@admin.register(Agriculteur)
class AgriculteurAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'bio')

@admin.register(Operateur)
class OperateurAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'address')

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('name', 'agriculteur', 'price', 'quantity_available', 'created_at')
    list_filter = ('agriculteur',)

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'operateur', 'produit', 'quantity', 'status', 'ordered_at')
    list_filter = ('status', 'operateur')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'commande', 'amount', 'transaction_date')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('produit', 'user', 'rating', 'comment')
    list_filter = ('produit', 'rating')

@admin.register(SuiviDeStock)
class SuiviDeStockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'current_quantity', 'alert_threshold')
