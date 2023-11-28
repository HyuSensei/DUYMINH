const axios = require("axios");
require("dotenv").config();

const indexproduct = async (req, res) => {
  try {
    let erro = req.flash("erro");
    let success = req.flash("success");
    const page = req.query.page || 1;
    const params = {
      page,
    };
    let data_product = await axios.get(
      process.env.BASE_URL + `admin/products`,
      { params }
    );
    return res.render("admin/dashboard.ejs", {
      products: data_product.data.products,
      current_page: data_product.data.current_page,
      total_page: data_product.data.total_page,
      erro,
      success,
    });
  } catch (error) {
    console.log(error);
  }
};

const getAddProduct = async (req, res) => {
  try {
    let erro = req.flash("erro");
    let success = req.flash("success");
    let data_category = await axios.get(
      process.env.BASE_URL + `admin/categories`
    );
    let data_brand = await axios.get(process.env.BASE_URL + `admin/brands`);
    return res.render("admin/create_product.ejs", {
      categories: data_category.data.categories,
      brands: data_brand.data.brand,
      erro,
      success,
    });
  } catch (error) {
    console.log(error);
  }
};

const storeProduct = async (req, res) => {
  try {
    // console.log("Data:", req.body);
    // console.log("Data:", req.file);
    if (req.file != null) {
      image = req.file.originalname;
    } else {
      image = "";
    }
    const data_product = {
      name: req.body.name,
      price: req.body.price,
      description: req.body.description,
      category_id: req.body.category_id,
      brand_id: req.body.brand_id,
      image: image,
    };
    console.log("Data:", data_product);
    let data = await axios.post(
      process.env.BASE_URL + `admin/products/store`,
      data_product
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect("/admin/products/create");
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect("/admin/products/create");
  }
};

const editProduct = async (req, res) => {
  try {
    let erro = req.flash("erro");
    let success = req.flash("success");
    let id = req.params.id;
    const data = await axios.get(process.env.BASE_URL + `products/${id}`);
    let data_category = await axios.get(
      process.env.BASE_URL + `admin/categories`
    );
    let data_brand = await axios.get(process.env.BASE_URL + `admin/brands`);
    return res.render("admin/edit_product.ejs", {
      product: data.data,
      categories: data_category.data.categories,
      brands: data_brand.data.brand,
      erro,
      success,
    });
  } catch (error) {
    console.log(error);
  }
};

const updateProduct = async (req, res) => {
  const product_id = req.body.id;
  try {
    if (req.file != null) {
      image = "/images/products/" + req.file.originalname;
    } else {
      image = "";
    }
    const data_product = {
      name: req.body.name,
      price: req.body.price,
      description: req.body.description,
      category_id: req.body.category_id,
      brand_id: req.body.brand_id,
      image: image,
    };
    console.log("Data:", data_product);
    let data = await axios.put(
      process.env.BASE_URL + `admin/products/update/${product_id}`,
      data_product
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect(`/admin/products/edit/${product_id}`);
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect(`/admin/products/edit/${product_id}`);
  }
};

const deleteProduct = async (req, res) => {
  const product_id = req.params.id;
  try {
    let data = await axios.delete(
      process.env.BASE_URL + `admin/products/delete/${product_id}`
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect(`/admin/products`);
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect(`/admin/products`);
  }
};

module.exports = {
  updateProduct,
  deleteProduct,
  indexproduct,
  getAddProduct,
  storeProduct,
  editProduct,
};
