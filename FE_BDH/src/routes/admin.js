const express = require("express");
const router = express.Router();
const apiAdmin = require("../api/admin/apiAdmin");
const apiUser = require("../api/admin/apiUser");
const apiProduct = require("../api/admin/apiProduct");
const apiCategory = require("../api/admin/apiCategory");
const apiBrand = require("../api/admin/apiBrand");
const apiOrderManagement = require("../api/admin/apiOrderManagement");
const upload = require("../middleware/UploadImg");
const middleware = require("../middleware/middleware");
// admin
router.get("/loginAdmin", apiAdmin.loginAdmin);
router.post("/loginAdmin", apiAdmin.handleLoginAdmin);
router.get("/logoutAdmin", (req, res) => {
  res.cookie("jwtadmin", "", { maxAge: 0 });
  res.cookie("adminUserId", "", { maxAge: 0 });
  res.cookie("adminname", "", { maxAge: 0 });
  res.cookie("adminemail", "", { maxAge: 0 });
  res.cookie("adminusername", "", { maxAge: 0 });
  res.cookie("adminaddress", "", { maxAge: 0 });
  return res.redirect("/loginAdmin");
});
//product
router.get(
  "/admin/products",
  middleware.checkPremission,
  apiProduct.indexproduct
);
router.get(
  "/admin/products/create",
  middleware.checkPremission,
  apiProduct.getAddProduct
);
router.post(
  "/admin/products/store",
  middleware.checkPremission,
  upload.single("image"),
  apiProduct.storeProduct
);
router.get(
  "/admin/products/edit/:id",
  middleware.checkPremission,
  apiProduct.editProduct
);
router.post(
  "/admin/products/update",
  middleware.checkPremission,
  upload.single("image"),
  apiProduct.updateProduct
);
router.get(
  "/admin/products/delete/:id",
  middleware.checkPremission,
  apiProduct.deleteProduct
);
//order
router.get(
  "/admin/orders",
  middleware.checkPremission,
  apiOrderManagement.indexOrder
);
router.get(
  "/admin/orders/delete/:id",
  middleware.checkPremission,
  apiOrderManagement.deleteOrder
);
router.get(
  "/admin/orders/confirm/:id",
  middleware.checkPremission,
  apiOrderManagement.confirmOrder
);
//user
router.get("/admin/users", middleware.checkPremission, apiUser.indexUser);
//category
router.get(
  "/admin/categories",
  middleware.checkPremission,
  apiCategory.indexCategory
);
router.get(
  "/admin/categories/create",
  middleware.checkPremission,
  (req, res) => {
    let erro = req.flash("erro");
    let success = req.flash("success");
    res.render("admin/create_category.ejs", { erro, success });
  }
);
router.get(
  "/admin/categories/edit/:id",
  middleware.checkPremission,
  apiCategory.editCategory
);
router.post(
  "/admin/categories/store",
  middleware.checkPremission,
  apiCategory.storeCategory
);
router.post(
  "/admin/categories/update",
  middleware.checkPremission,
  apiCategory.updateCategory
);
router.get(
  "/admin/categories/delete/:id",
  middleware.checkPremission,
  apiCategory.deleteCategory
);
//brand
router.get("/admin/brands", middleware.checkPremission, apiBrand.indexBrand);
router.get("/admin/brands/create", middleware.checkPremission, (req, res) => {
  let erro = req.flash("erro");
  let success = req.flash("success");
  res.render("admin/create_brand.ejs", middleware.checkPremission, {
    erro,
    success,
  });
});
router.get(
  "/admin/brands/edit/:id",
  middleware.checkPremission,
  apiBrand.editBrand
);
router.post(
  "/admin/brands/store",
  middleware.checkPremission,
  apiBrand.storeBrand
);
router.post(
  "/admin/brands/update",
  middleware.checkPremission,
  apiBrand.updateBrand
);
router.get(
  "/admin/brands/delete/:id",
  middleware.checkPremission,
  apiBrand.deleteBrand
);

router.get("/logoutAdmin", (req, res) => {
  res.cookie("jwtadmin", "", { maxAge: 0 });
  res.cookie("adminUserId", "", { maxAge: 0 });
  res.cookie("adminname", "", { maxAge: 0 });
  res.cookie("adminemail", "", { maxAge: 0 });
  res.cookie("adminusername", "", { maxAge: 0 });
  res.cookie("adminaddress", "", { maxAge: 0 });
  return res.redirect("/loginAdmin");
});
module.exports = router;
