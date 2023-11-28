const axios = require("axios");
require("dotenv").config();
const indexBrand = async (req, res) => {
  try {
    let erro = req.flash("erro");
    let success = req.flash("success");
    const page = req.query.page || 1;
    const params = {
      page,
    };
    let data_product = await axios.get(process.env.BASE_URL + `admin/brands`, {
      params,
    });
    return res.render("admin/brand.ejs", {
      brands: data_product.data.brand,
      current_page: data_product.data.current_page,
      total_page: data_product.data.total_page,
      erro,
      success,
    });
  } catch (error) {
    console.log(error);
  }
};
const storeBrand = async (req, res) => {
  try {
    let data = await axios.post(
      process.env.BASE_URL + `admin/brands/store`,
      req.body
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect("/admin/brands/store");
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect("/admin/brands/create");
  }
};
const editBrand = async (req, res) => {
  try {
    let erro = req.flash("erro");
    let success = req.flash("success");
    let id = req.params.id;
    const data = await axios.get(process.env.BASE_URL + `admin/brands/${id}`);
    return res.render("admin/edit_brand.ejs", {
      brand: data.data.brand,
      erro,
      success,
    });
  } catch (error) {
    console.log(error);
  }
};
const updateBrand = async (req, res) => {
  const brand_id = req.body.id;
  try {
    let data = await axios.put(
      process.env.BASE_URL + `admin/brands/update/${brand_id}`,
      req.body
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect(`/admin/brands/edit/${brand_id}`);
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect(`/admin/brands/edit/${brand_id}`);
  }
};
const deleteBrand = async (req, res) => {
  const brand_id = req.params.id;
  try {
    let data = await axios.delete(
      process.env.BASE_URL + `admin/brands/delete/${brand_id}`
    );
    if (data.data.success !== false) {
      req.flash("success", `${data.data.message}`);
      res.redirect(`/admin/brands`);
    }
  } catch (error) {
    console.log(error);
    req.flash("erro", `${error.response.data.detail}`);
    res.redirect(`/admin/brands`);
  }
};

module.exports = {
  indexBrand,
  editBrand,
  updateBrand,
  deleteBrand,
  storeBrand,
};
