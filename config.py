#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "17073544"))
    API_HASH = os.environ.get("API_HASH", "f2a07b0eb2ddafc88dee6ea35bbbf2c2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6146463402:AAGiO-ZEwpEcFxWAIwQfmuVwrNGiKUzD6vU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "5015968435")
    LIMIT = int(os.environ.get("LIMIT", "100000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQCY8Fc0Kc_W76wZ5KGme4BGH25ba7EIpCqTf7g-fs0-rVlmflcsL_nvGoIR2qs-uT2DxxTu41AY0uHLxVehOBm7WupfX7WJwXOjSW2OggGFEv6fR96b1kcUCr2SawDFm97bSZ1gBzH64VPxdgLY2MVCJ89l4yQOC8WjL9Arq2wMP4MlSVsNPOx4m36ow1HOrwSdBWjbdIPKumt8ytkOsL5qbJNf7irYoGM78Todd3PhW4xcgj4lMfZetztnmkSyBo4uLpMIQH6j6kaXXL4VcCm2ftCmro23Dg7pXac2iFBrk36nnVyI7SSCm_SHODghiTiKOHs1M-AiyRy7a1nE1L0UAAAAASr5mrMA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001714981648"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
