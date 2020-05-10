# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class BookingType(models.Model):
    """
    Booking type model.

    TODO: Add description.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("User that owns this booking type.")
    )
    name = models.CharField(
        max_length=60,
        help_text=_("Name of booking type, shown to users picking a meeting.")
    )
    slug = models.SlugField(
        max_length=20,
        help_text=_("Custom slug for meeting type, must be unique per user.")
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Pretty string representation of model.

        Note that this has a call to a relational model,
        and needs the appropriate `.select_related` selector
        to avoid a huge amount of queries.
        """
        return f"[{self.owner}] {self.name}."


class BookingAvailability(models.Model):
    """
    BookingAvailability model.

    TODO: Add description.
    """
    booking_type = models.OneToOneField(
        BookingType,
        on_delete=models.CASCADE,
        help_text=_("Booking type associated with this model.")
    )

    # Meeting attributes
    duration = models.DurationField(
        default=timedelta(minutes=30),
        help_text=_("Meeting duration, used for creating booking slots.")
    )
    padding = models.DurationField(
        default=timedelta(minutes=5),
        help_text=_("Minimum allowed amount of time between 2 meetings.")
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Pretty string representation of model.

        Note that this has a call to a relational model,
        and needs the appropriate `.select_related` selector
        to avoid a huge amount of queries.
        """
        return f"[{self.booking_type}] {self.duration}."
