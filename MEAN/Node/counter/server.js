// require express
var express = require("express");
// path module -- try to figure out where and why we use this
var path = require("path");

var session = require('express-session');
var app = express();
app.use(session({secret: 'codingdojorocks'})); 

// create the express app
var bodyParser = require('body-parser');


// use it!
app.use(bodyParser.urlencoded({ extended: true }));

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

// static content
app.use(express.static(path.join(__dirname, "./static")));


app.get('/', function (req, res){
    if(!req.session['count']) {
        req.session['count'] = 0;
    }
    req.session.count +=1;
    res.render('index', { count : req.session.count});
});

app.get('/add', function (req,res){
    req.session.count+=1;
    res.redirect('/');
});

app.get('/reset', function (req,res){
    req.session.count = 0;
    res.redirect('/');
});

// tell the express app to listen on port 8000
app.listen(8000, function() {
 console.log("listening on port 8000");
});
