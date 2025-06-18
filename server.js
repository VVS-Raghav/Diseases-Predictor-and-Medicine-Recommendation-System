const express = require("express");
const bodyParser = require("body-parser");
const { PythonShell } = require("python-shell");
const Symptoms = require('./symptoms.json'); 
const path = require("path");

const app = express();
app.set("view engine", "ejs");
app.set("views", __dirname+ "/views");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index",{symptoms:Object.keys(Symptoms)});
});

app.post("/predict", (req, res) => {
  let symptoms = req.body.symptoms;

  if (!symptoms || (Array.isArray(symptoms) && symptoms.length === 0)) {
    return res.render("index", {
      message: "Please select at least one symptom.",
      symptoms: Object.keys(Symptoms)
    });
  }

  if (!Array.isArray(symptoms)) {
    symptoms = [symptoms];
  }

  const symptomsArg = symptoms.join(",");

  const options = {
    mode: "text",
    pythonOptions: ["-u"],
    scriptPath: "./",
    args: [symptomsArg],
  };

  PythonShell.run("predict.py", options).then((results) => {
    const data = JSON.parse(results[0]);
    res.render("index", data);
  }).catch((err) => {
    console.error("Python error:", err);
    res.render("index", { message: "Prediction failed, please try again." });
  });
});

app.listen(3000, () => {
  console.log("Server started on http://localhost:3000");
});
