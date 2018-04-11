var path = require('path');
var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var app = express();

mongoose.connect('mongodb://localhost/1955_api');
mongoose.Promise = global.Promise; 

var PeopleSchema = new mongoose.Schema({
    name: String
})
mongoose.model('People', PeopleSchema);
var People = mongoose.model("People")


app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');


app.get('/', function(req, res) {
    People.find({}, function(err, peoples) {
        if(err) {
            console.log('something went wrong', err);
            res.json({message: "error", error: err});
        } else {
            res.json({message: 'success', {peoples: peoples});
        }
    })
})


app.get('/new/:name/', function(req, res) {
    console.log(req.params.name);
    var people = new People({name: req.params.name});
    people.save(function(err) {
        if(err) {
            console.log('something went wrong', err);
            res.json({message: "error", error: err});
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