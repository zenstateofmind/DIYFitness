from enum import Enum


class Movement:
    def __init__(self, benefits, body_parts, injuries, intensity):
        self.benefits = benefits
        self.body_parts = body_parts
        self.injuries = injuries
        self.intensity = intensity


class BodyPart:
    def __init__(self, name, definition):
        self.name = name
        self.definition = definition


class Intensity(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3


class Injury:
    def __init__(self, name, definition, bodyparts_impacted):
        self.name = name
        self.definition = definition
        self.bodyparts_impacted = bodyparts_impacted


class WorkoutSection:
    def __init__(self, movements, time_gap):
        self.movements = movements
        self.time_gap = time_gap


class WarmUpSection(WorkoutSection):
    def __init__(self, movements, intro_script):
        WorkoutSection.__init__(movements=movements, time_gap=0)
        self.intro_script = intro_script


class MainMovementSection(WorkoutSection):
    def __init__(self, movements, time_gap, num_rounds):
        WorkoutSection.__init__(movements=movements, time_gap=time_gap)
        self.num_rounds = num_rounds


class CoolDownSection(WorkoutSection):
    def __init__(self, movements, outro_script):
        WorkoutSection.__init__(movements=movements, time_gap=0)
        self.outro_script = outro_script


class Workout:
    def __init__(self, warmup_section, mainmovement_section, cooldown_section):
        self.warmup_section = warmup_section
        self.mainmovement_section = mainmovement_section
        self.cooldown_section = cooldown_section


class Pack:
    def __init__(self, workouts, intensity):
        self.workouts = workouts
        self.intensity = intensity

