var path = require('path');
var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var app = express();

mongoose.connect('mongodb://localhost/animal_dojo');
mongoose.Promise = global.Promise; 

var AnimalSchema = new mongoose.Schema({
    name: String,
    age: Number,
    created_at: String
})
mongoose.model('Animal', AnimalSchema);
var Animal = mongoose.model("Animal")


app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');


app.get('/', function(req, res) {
    Animal.find({}, function(err, animals) {
        if(err) {
            console.log('something went wrong');
        } else {
            res.render('index', {animals: animals});
        }
    })
})

app.get('/animals/new', function(req, res) {
    res.render('new');
})

app.post('/animals', function(req, res) {
    console.log("POST DATA", req.body);
    var animal = new Animal({name: req.body.name, age: req.body.age, created_at: Date()});
    animal.save(function(err) {
        if(err) {
            console.log('something went wrong');
        } else {
            console.log('successfully added a user!');
            res.redirect('/');
        }
    })
})

app.get('/animals/:id', function(req, res) {
    console.log(req.params.id);
    Animal.find({_id:req.params.id}, function(err, animals) {
        if(err) {
            console.log('no animal')
        } else {
            console.log('found animal');
            res.render('bio', {animals: animals} );
        }
    })
})

app.get('/animals/edit/:id', function(req, res) {
    Animal.find({_id:req.params.id}, function(err, animals) {
        if(err) {
            console.log('no animal')
        } else {
            console.log('found animal');
            res.render('edit', {animals: animals} );
        }
    })
})

app.post('/animals/:id', function(req, res) {
    console.log(req.params.id);
    Animal.findOne({_id:req.params.id}, function(err, animal) {
        if(err) {
            console.log('no animal')
        } else {
            animal.name = req.body.name;
            animal.age = req.body.age;
            animal.save(function(err) {
                if(err){
                    console.log('didnt edit');
                    console.log(err)
                    res.redirect('/edit')
                } else {
                    console.log('edited animal save');
                    console.log(animal)
                    res.redirect('/');  
                }  
            })
        }
    })
})

app.post('/animals/destroy/:id', function(req, res) {
    Animal.remove({_id:req.params.id}, function(err) {
        if(err){
            console.log("didn't delete");
            console.log(err);
            res.redirect('/edit')
        } else {
            console.log('deleted animal');
            res.redirect('/')
        }
    })
})

app.listen(8000, function() {
    console.log("listening on port 8000");
})