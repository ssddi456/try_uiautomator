var express = require('express');
var router = express.Router();

var fs = require('fs');
var path = require('path');


var logFile = path.join(__dirname, '../data/test_log');
console.log( 'logFile', logFile);
/* GET users listing. */
router.post('/', function(req, res, next) {
  fs.appendFileSync(logFile, JSON.stringify({
      ua: req.headers['user-agent'],
      res: req.body
  }) + '\n');
  res.json({err:0});
});

router.get('/', function(req, res, next) {
  res.end(fs.readFileSync(logFile, 'utf8'));
})
module.exports = router;
