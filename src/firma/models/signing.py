from django.db import models
from django.utils.translation import ugettext_lazy as _


class Signing(models.Model):
    full_name = models.CharField(
        verbose_name=_("Nombre completo"),
        max_length=140,
        null=True,
        blank=True
    )

    original_string = models.TextField(
        verbose_name=_("Cadena original"),
        null=True,
        blank=True
    )

    invoice = models.CharField(
        verbose_name=_("Folio de consulta"),
        max_length=150,
        null=True,
        blank=True
    )

    signing_type = models.CharField(
        verbose_name=_("Tipo de firma"),
        max_length=50,
        null=True,
        blank=True
    )

    user = models.CharField(
        verbose_name=_("Usuario verificado"),
        max_length=80,
        null=True,
        blank=True
    )

    curp = models.CharField(
        verbose_name=_("CURP"),
        max_length=18,
        null=True,
        blank=True
    )

    rfc = models.CharField(
        verbose_name=_("R.F.C."),
        max_length=13,
        null=True,
        blank=True
    )

    query_sat = models.CharField(
        verbose_name=_("Consulta SAT"),
        max_length=20,
        null=True,
        blank=True
    )

    status_cert = models.CharField(
        verbose_name=_("Estatus certificado"),
        max_length=50,
        null=True,
        blank=True
    )

    stamp = models.TextField(
        verbose_name=_("Sello"),
        null=True,
        blank=True
    )
     
    active = models.BooleanField(
        verbose_name=("Activo"),
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _("firma")
        verbose_name_plural = _("firmas")

    def __str__(self):
        return self.rfc

    # def get_absolute_url(self):
    #     return reverse("Signing_detail", kwargs={"pk": self.pk})
