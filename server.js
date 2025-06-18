const express = require("express");
const bodyParser = require("body-parser");
const { PythonShell } = require("python-shell");
const path = require("path");

const app = express();
app.set("view engine", "ejs");
app.set("views", __dirname+ "/views");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index");
});

app.post("/predict", (req, res) => {
  const symptoms = req.body.symptoms;

  if (!symptoms || symptoms === "Symptoms") {
    return res.render("index", {
      message: "Please either write symptoms or you have written misspelled symptoms",
    });
  }

  const options = {
    mode: "text",
    pythonOptions: ["-u"],
    scriptPath: "./",
    args: [symptoms],
  };

  PythonShell.run("predict.py", options).then((results) => {
    const data = JSON.parse(results[0]);
    res.render("index", data);
  }).catch((err) => {
    console.error("Python error:", err);
    res.render("index", { message: "Prediction failed, please try again." });
  });
});

app.get("/about", (req, res) => res.render("about"));
app.get("/contact", (req, res) => res.render("contact"));
app.get("/developer", (req, res) => res.render("developer"));
app.get("/blog", (req, res) => res.render("blog"));

app.listen(3000, () => {
  console.log("Server started on http://localhost:3000");
});
