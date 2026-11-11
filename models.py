from sqlmodel import Field , SQLModel

class FoodPreference(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    favorite_food: str
    favorite_drinks: str
    favorite_dessert: str
    favorite_fastfood: str
    preferred_cuisine: str
    spicy_food: str
    eating_frequency: str
    food_allergies: str




