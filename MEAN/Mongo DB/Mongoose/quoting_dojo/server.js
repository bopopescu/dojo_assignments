var path = require('path');
var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var app = express();

mongoose.connect('mongodb://localhost/quoting_dojo');
mongoose.Promise = global.Promise; 

var QuoteSchema = new mongoose.Schema({
    name: String,
    quote: String,
    created_at: String
})
mongoose.model('Quote', QuoteSchema); 
var Quote = mongoose.model('Quote') 

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');


app.get('/', function(req, res) {
    // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
    res.render('index');
})

app.post('/process', function(req, res) {
    console.log("POST DATA", req.body);
    var quote = new Quote({name: req.body.name, quote: req.body.quote, created_at: Date()});
    quote.save(function(err) {
        if(err) {
            console.log('something went wrong');
        } else {
            console.log('successfully added a user!');
            res.redirect('/quotes');
        }
    })
})
 
app.get('/quotes', function(req, res) {
    Quote.find({}, function(err, quotes) {
        if(err) {
            console.log('something went wrong');
        } else {
            console.log(quotes);
            res.render('quotes', {quotes: quotes});
        }
    })
})


app.listen(8000, function() {
    console.log("listening on port 8000");
})