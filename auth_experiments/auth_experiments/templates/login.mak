<%inherit file="layout/layout.mak"/>
<form method="post">
  <div class="row">
     <div class="large-8 large-centered columns" id="login-title">
     <h1>MyHRMS</h1>
     </div>
  </div>
  <div class="row">
    <div class="large-8 large-centered columns">
      <div class="row">
        <div class="large-3 columns">
          <label for="email" class="right inline">E-Mail</label>
        </div>
        <div class="large-9 columns">
          <input type="text" name="email" id="email" placeholder="Your email here"/>
        </div>
      </div>
      <div class="row">
        <div class="large-3 columns">
          <label for="password" class="right inline">Password</label>
        </div>
        <div class="large-9 columns">
          <input type="password" name="password" id="password" placeholder="Password here"/>
        </div>
      </div>
      <div class="row">
	<div class="large-3 large-offset-9 columns">
	   <input type="submit" name="form.submitted" class="button radius small expand" value="Login >>"></input>
	</div>	
      </div>
    </div>
  </div>
</form>
