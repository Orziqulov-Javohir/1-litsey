from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Sentyabr_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar Sentyabr'
        verbose_name_plural = '1 -kurslar Sentyabr'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Sentyabr_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH
      
class Oktyabr_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar Oktyabr'
        verbose_name_plural = '1 -kurslar Oktyabr'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Oktyabr_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH      

class Noyabr_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar Noyabr'
        verbose_name_plural = '1 -kurslar Noyabr'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Noyabr_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  
  

class Dekabr_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar Dekabr'
        verbose_name_plural = '1 -kurslar Dekabr'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Dekabr_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  
    

class Yanvar_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar Yanvar'
        verbose_name_plural = '1 -kurslar Yanvar'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Yanvar_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  
    
class Fevral_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar Fevral'
        verbose_name_plural = '1 -kurslar Fevral'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Fevral_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH
    
class Mart_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar Mart'
        verbose_name_plural = '1 -kurslar Mart'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Mart_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  


class Aprel_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar Aprel'
        verbose_name_plural = '1 -kurslar Aprel'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Aprel_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  


class May_1(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '1 -kurslar May'
        verbose_name_plural = '1 -kurslar May'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(May_1, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  

class Sentyabr_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar Sentyabr'
        verbose_name_plural = '2 -kurslar Sentyabr'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Sentyabr_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  
      
class Oktyabr_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar Oktyabr'
        verbose_name_plural = '2 -kurslar Oktyabr'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Oktyabr_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH      

class Noyabr_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar Noyabr'
        verbose_name_plural = '2 -kurslar Noyabr'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Noyabr_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  
  

class Dekabr_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar Dekabr'
        verbose_name_plural = '2 -kurslar Dekabr'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Dekabr_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  
    

class Yanvar_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar Yanvar'
        verbose_name_plural = '2 -kurslar Yanvar'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Yanvar_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  
    
class Fevral_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar Fevral'
        verbose_name_plural = '2 -kurslar Fevral'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Fevral_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH
    
class Mart_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar Mart'
        verbose_name_plural = '2 -kurslar Mart'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Mart_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  


class Aprel_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar Aprel'
        verbose_name_plural = '2 -kurslar Aprel'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(Aprel_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH   


class May_2(models.Model):
    F_I_SH = models.CharField(max_length=255, null = True)
    Guruh = models.CharField(max_length=255,null = True)
    Ona_tili = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Matem = models.IntegerField(null = True, default = 0,validators=[MinValueValidator(0), MaxValueValidator(15)])
    Tarix = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    blok_1 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    blok_2 = models.IntegerField(null = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    Jami = models.DecimalField(null = True, blank=True, decimal_places=1, max_digits=4)

    class Meta:
        ordering = ['-Jami']
        verbose_name = '2 -kurslar May'
        verbose_name_plural = '2 -kurslar May'
        
    def save(self):
        self.Jami = (self.Tarix + self.Ona_tili + self.Matem) * 2.1 + (self.blok_1 + self.blok_2) * 3.1 
        super(May_2, self).save()
        
    def __str__(self):
        return str(self.Jami) + " ball  / " +  self.F_I_SH  