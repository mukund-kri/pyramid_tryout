<!DOCTYPE html>
<!--[if IE 8]>         <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width" />
  <title>MyHRMS</title>

  <link rel="stylesheet" href="/static/css/normalize.css" />
  <!-- If you are using CSS version, add this -->
  <link rel="stylesheet" href="/static/css/foundation.css" />
  <link rel="stylesheet" href="/static/css/app.css" />

  <script src="/static/js/vendor/custom.modernizr.js"></script>

</head>
<body>

  <!-- body content here -->
  ${next.body()}

  <script>
  document.write('<script src=' +
  ('__proto__' in {} ? '/static/js/vendor/zepto' : '/staic/js/vendor/jquery') +
  '.js><\/script>')
  </script>
  <script src="/static/js/foundation/foundation.js"></script>
  <script>
  $(document).foundation();
  </script>
</body>
</html>