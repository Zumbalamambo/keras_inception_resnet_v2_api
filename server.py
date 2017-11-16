# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very simple flask server to serve models."""

from models import modelserver
import settings
import sys
sys.path.append("./models")

modelserver.initialize_models(json_path=settings.path_model_json,
                              weights_path=settings.path_model_weight,
                              normalized_x=settings.path_x_normalizer,
                              normalized_y=settings.path_y_normalizer)
modelserver.run()
