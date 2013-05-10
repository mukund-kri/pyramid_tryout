<!DOCTYPE html>
<!--[if IE 8]>         <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" lang="en">
  <!--<![endif]-->

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Foundation 4</title>

    <link rel="stylesheet" href="/static/css/normalize.css" />
    <!-- If you are using CSS version, add this -->
    <link rel="stylesheet" href="/static/css/foundation.css" />
    <link rel="stylesheet" href="/static/css/app.css" />

    <script src="/static/js/vendor/custom.modernizr.js"></script>

  </head>
  <body>
    <nav class="top-bar">
      <ul class="title-area">
        <!-- Title Area -->
        <li class="name">
          <h1><a href="#"> HR App </a></h1>
        </li>
      </ul>
      <section class="top-bar-section">
        <!-- Right Nav Section -->
        <ul class="right">
          <li class="divider"></li>
          <li>
            <a href="#">User Admin</a>
          </li>
        </ul>
      </section>
    </nav>
    <div class="row">
      <div class="large-9 push-3 columns">
        ${next.body()}
      </div>
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
    <script src="/static/js/foundation/foundation.alerts.js"></script>
    <script src="/static/js/foundation/foundation.clearing.js"></script>
    <script src="/static/js/foundation/foundation.cookie.js"></script>
    <script src="/static/js/foundation/foundation.dropdown.js"></script>
    <script src="/static/js/foundation/foundation.forms.js"></script>
    <script src="/static/js/foundation/foundation.joyride.js"></script>
    <script src="/static/js/foundation/foundation.magellan.js"></script>
    <script src="/static/js/foundation/foundation.orbit.js"></script>
    <script src="/static/js/foundation/foundation.placeholder.js"></script>
    <script src="/static/js/foundation/foundation.reveal.js"></script>
    <script src="/static/js/foundation/foundation.section.js"></script>
    <script src="/static/js/foundation/foundation.tooltips.js"></script>
    <script src="/static/js/foundation/foundation.topbar.js"></script>
    <script>
		$(document).foundation();
    </script>
  </body>
</html>