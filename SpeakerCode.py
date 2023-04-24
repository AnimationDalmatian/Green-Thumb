import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

#using pygame mixer to play audio file
soundfiles = ["one.wav", "two.wav", "three.wav", "four.wav"]
sounds = [pygame.mixer.Sound(name) for name in soundfiles]




