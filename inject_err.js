const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const errLogger = `
<script>
  window.addEventListener('error', function(e) {
    const errDiv = document.createElement('div');
    errDiv.style.cssText = 'position:fixed; top:0; left:0; right:0; background:red; color:white; z-index:999999; padding:20px; font-size:12px;';
    errDiv.innerHTML = "ERROR: " + e.message + " <br> at " + e.filename + ":" + e.lineno;
    document.body.appendChild(errDiv);
  });
</script>
</head>
`;

html = html.replace('</head>', errLogger);
fs.writeFileSync('index.html', html, 'utf8');
console.log("Injected error logger");
