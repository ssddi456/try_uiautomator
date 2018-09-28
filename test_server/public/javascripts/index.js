var tests = {
  'https://jin.baidu.com': 'https://jin.baidu.com/',
  'https://icash.baidu.com': 'https://icash.baidu.com/static/cloan/pkg/image/page/activity/pinzhuan/pinzhuan-pc/img/pc-header_18df318.png',
  'https://www.baifubao.com': 'https://www.baifubao.com/',
  'https://co.baifubao.com': 'https://co.baifubao.com/content/pc_wallet_index/images/index-img-slider-0.jpg',
};

function msgBlock(msg) {
    var div = document.createElement('div');
    div.innerHTML = msg;
    div.className = 'test-log';
    document.body.appendChild(div);
}

function debug() {
    var args = [].slice.call(arguments);
    // console.log.apply(console, args);
    // return;
    var msg = args.map(function (arg) {
        return JSON.stringify(arg);
    }).join(' ');
    msgBlock(msg);
}

window.onerror = function(e) {
    debug(e.message);
    debug(e.stack);
}

console.log = debug;

function sendImage(src, done) {
  console.log( 'sendImage', src);
  var img = new Image();
  img.onload = function() {
    done && done();
  };
  img.onerror = function(e) {
    console.log('img load error', e);
    done && done('failed');
  };
  img.src = src;
  document.body.appendChild(img);
}

var res = [];
var promises = [];
for (var k in tests) {
  (function(domain, src) {
    promises.push(new Promise(function(resolve) {
      sendImage(src, function(err) {
        res.push({
          domain: domain,
          banned: !!err
        });
        resolve();
      })
    }));
  }(k, tests[k]));
}

Promise.all(promises).then(function() {
  sendlog(res);
});

function sendlog() {
  var query = JSON.stringify(res);
  fetch('/test_log', {
    method: 'POST',
    headers: {
      'content-type': 'application/json'
    },
    body: query
  });
}