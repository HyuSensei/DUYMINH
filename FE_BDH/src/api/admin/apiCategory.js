const axios = require("axios");
require("dotenv").config();
const indexCategory = async (req, res) => {
  try {
    let erro = req.flash("erro");
    let success = req.flash("success");
    const page = req.query.page || 1;
    const params = {
      page,
    };
    let data_product = await axios.get(
      process.env.BASE_URL + `admin/categories`,
      {
        params,
      }
    );
    return res.render("admin/category.ejs", {
      categories: data_product.data.categories,
      current_page: data_product.data.current_page,
      total_page: data_product.data.total_page,
      erro,
      success,
    });
  } catch (error) {
    console.log(error);
  }
};
const storeCategory = async (req, res) => {
  try {
    let data = await axios.post(
      process.env.BASE_URL + `admin/categories/store`,
      req.body
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect("/admin/categories/create");
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect("/admin/categories/create");
  }
};
const editCategory = async (req, res) => {
  try {
    let erro = req.flash("erro");
    let success = req.flash("success");
    let id = req.params.id;
    const data = await axios.get(
      process.env.BASE_URL + `admin/categories/${id}`
    );
    console.log(data.data);
    return res.render("admin/edit_category.ejs", {
      category: data.data.category,
      erro,
      success,
    });
  } catch (error) {
    console.log(error);
  }
};
const updateCategory = async (req, res) => {
  const category_id = req.body.id;
  try {
    let data = await axios.put(
      process.env.BASE_URL + `admin/categories/update/${category_id}`,
      req.body
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect(`/admin/categories/edit/${category_id}`);
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect(`/admin/categories/edit/${category_id}`);
  }
};
const deleteCategory = async (req, res) => {
  const category_id = req.params.id;
  try {
    let data = await axios.delete(
      process.env.BASE_URL + `admin/categories/delete/${category_id}`
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect(`/admin/categories`);
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect(`/admin/categories`);
  }
};

module.exports = {
  indexCategory,
  editCategory,
  updateCategory,
  deleteCategory,
  storeCategory,
};
