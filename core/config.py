import decouple


class Settings:
    WATER_MARK = decouple.config("WATER_MARK")
