from django.db import models

class Citoyen(models.Model):
    # Choix pour les champs
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('A', 'Autre'),
    ]
    
    SITUATION_FAMILIALE_CHOICES = [
        ('C', 'Célibataire'),
        ('M', 'Marié(e)'),
        ('D', 'Divorcé(e)'),
        ('V', 'Veuf/Veuve'),
        ('U', 'Union libre'),
    ]
    
    SITUATION_PROFESSIONNELLE_CHOICES = [
        ('A', 'Actif'),
        ('C', 'Chômeur'),
        ('E', 'Étudiant'),
        ('R', 'Retraité'),
        ('I', 'Indépendant'),
        ('F', 'Fonctionnaire'),
    ]
    
    NIVEAU_EDUCATION_CHOICES = [
        ('P', 'Primaire'),
        ('S', 'Secondaire'),
        ('B', 'Baccalauréat'),
        ('U', 'Universitaire'),
        ('M', 'Master'),
        ('D', 'Doctorat'),
    ]
    
    GROUPES_SANGUINS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    # === INFORMATIONS PERSONNELLES ===
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=200)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=200)
    nationalite = models.CharField(max_length=100, default='Malagasy')
    situation_familiale = models.CharField(max_length=1, choices=SITUATION_FAMILIALE_CHOICES, default='C')
    
    # === DOCUMENTS D'IDENTITÉ ===
    numero_cin = models.CharField(max_length=20, unique=True)
    numero_passeport = models.CharField(max_length=20, blank=True, null=True)
    numero_securite_sociale = models.CharField(max_length=30, blank=True, null=True)
    numero_contribuable = models.CharField(max_length=20, blank=True, null=True)
    
    # === INFORMATIONS DE RÉSIDENCE ===
    adresse = models.TextField()
    province = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True, null=True)
    commune = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    # === INFORMATIONS PROFESSIONNELLES ===
    profession = models.CharField(max_length=100, blank=True, null=True)
    employeur = models.CharField(max_length=100, blank=True, null=True)
    secteur_activite = models.CharField(max_length=100, blank=True, null=True)
    situation_professionnelle = models.CharField(max_length=1, choices=SITUATION_PROFESSIONNELLE_CHOICES, default='A')
    revenu_annuel = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    
    # === INFORMATIONS ÉDUCATIVES ===
    niveau_education = models.CharField(max_length=1, choices=NIVEAU_EDUCATION_CHOICES, blank=True, null=True)
    diplome = models.CharField(max_length=100, blank=True, null=True)
    etablissement = models.CharField(max_length=200, blank=True, null=True)
    
    # === INFORMATIONS SANITAIRES ===
    groupe_sanguin = models.CharField(max_length=3, choices=GROUPES_SANGUINS, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    couverture_medicale = models.BooleanField(default=False)
    nom_medecin_traitant = models.CharField(max_length=100, blank=True, null=True)
    
    # === INFORMATIONS CIVIQUES ===
    bureau_vote = models.CharField(max_length=100, blank=True, null=True)
    circonscription_electorale = models.CharField(max_length=100, blank=True, null=True)
    situation_militaire = models.CharField(max_length=100, blank=True, null=True)
    
    # === MÉTADONNÉES ===
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    est_actif = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos_citoyens/', blank=True, null=True)
    empreinte_digitale = models.BinaryField(blank=True, null=True)  # Pour identification biométrique
    
    # === INFORMATIONS DES PARENTS ===
    nom_pere = models.CharField(max_length=100, blank=True, null=True)
    nom_mere = models.CharField(max_length=100, blank=True, null=True)
    profession_pere = models.CharField(max_length=100, blank=True, null=True)
    profession_mere = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Citoyen"
        verbose_name_plural = "Citoyens"
        ordering = ['nom', 'prenoms']
        indexes = [
            models.Index(fields=['numero_cin']),
            models.Index(fields=['nom', 'prenoms']),
            models.Index(fields=['province', 'commune']),
        ]

    def __str__(self):
        return f"{self.nom} {self.prenoms} - {self.numero_cin}"

    def age(self):
        """Calcule l'âge à partir de la date de naissance"""
        from datetime import date
        today = date.today()
        return today.year - self.date_naissance.year - (
            (today.month, today.day) < (self.date_naissance.month, self.date_naissance.day)
        )

    @property
    def nom_complet(self):
        return f"{self.nom} {self.prenoms}"

    def adresse_complete(self):
        return f"{self.adresse}, {self.quartier}, {self.commune}, {self.province}"