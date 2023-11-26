from fastapi import  FastAPI
import models
from database import engine
from routes.user import auth,product,brand,category,order
from routes.admin import auth as authAdmin, product as productAdmin, user, category as categoryAdmin, roles, order as orderAdmin
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(brand.router)
app.include_router(category.router)
app.include_router(order.router)


app.include_router(authAdmin.router)
app.include_router(productAdmin.router)
app.include_router(user.router)
app.include_router(categoryAdmin.router)
app.include_router(roles.router)
app.include_router(orderAdmin.router)