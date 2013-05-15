<!DOCTYPE html>
<!--[if IE 8]>         <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" lang="en">
  <!--<![endif]-->

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>My HRMS</title>

    <link rel="stylesheet" href="/static/css/normalize.css" />
    <!-- If you are using CSS version, add this -->
    <link rel="stylesheet" href="/static/css/foundation.css" />
    <link rel="stylesheet" href="/static/css/app.css" />
    
    <script src="/static/js/vendor/custom.modernizr.js"></script>
    
  </head>
  <body>
    <!-- Top navigation -->
    <nav class="top-bar">
      <ul class="title-area">
        <li class="name">
          <h1><a href="#"> HR App </a></h1>
        </li>
      </ul>
      <section class="top-bar-section">
        <ul class="right">
          <li class="divider"></li>
          <li>
            <a href="#">User Admin</a>
          </li>
        </ul>
      </section>
    </nav>
    <div class="row">
      <!-- Main content -->
      <div class="large-9 push-3 columns">
        ${next.body()}
      </div>
      <!-- Left navigation -->
      <div class="large-3 pull-9 columns">
        <ul class="side-nav">
          <li>
            <a href="#">Section 1</a>
          </li>
      </div>
    </div>

    <script>
		document.write('<script src=' + ('__proto__' in {} ? '/static/js/vendor/zepto' : '/staic/js/vendor/jquery') + '.js><\/script>')
    </script>
    <script src="/static/js/foundation/foundation.js"></script>
    <script>
		$(document).foundation();
    </script>
  </body>
</html>