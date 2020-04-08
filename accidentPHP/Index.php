<!doctype html>
<html lang="en">
  <head>

    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>Accident Detection Using Vanet</title>
    <meta content="" name="descriptison">
    <meta content="" name="keywords">

    <link href="assets/img/favicon.png" rel="icon">
    <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">


    <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">



    <link href="assets/css/style.css" rel="stylesheet">


    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.2.1/css/ol.css" type="text/css">
    <link rel="stylesheet" type="text/css" href="./css/styles.css">
    <script src="https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.2.1/build/ol.js"></script>
    
  </head>



  <body>

    <section id="hero">
      <div class="hero-container">
        <a href="index.html" class="hero-logo" data-aos="zoom-in"><img src="assets/img/hero-logo.png" alt=""></a>
        <h1 data-aos="zoom-in">Welcome</h1>
        <h2 data-aos="fade-up">Technology Can Save Lives</h2>
        <a data-aos="fade-up" href="#about" class="btn-get-started scrollto">Lets Change Lives</a>
      </div>
    </section>


    <header id="header" class="d-flex align-items-center">
      <div class="container">

        <div class="logo d-block d-lg-none">
          <a href="index.html"><img src="assets/img/logo.png" alt="" class="img-fluid"></a>
        </div>

        <nav class="nav-menu d-none d-lg-block">
          <ul class="nav-inner">
            <li class="nav-logo"><a href="index.html"><img src="assets/img/logo.png" alt="" class="img-fluid"></a></li>
          </ul>
        </nav>

      </div>
    </header>

    <main id="main">


      <section id="about" class="about">
        <div class="container">

          <div class="section-title" data-aos="fade-up">
            <h2>DataBase Values</h2>
            </br></br>
  
            <table class="table">
              <thead class="thead-dark">
                <tr>
                  <th scope="col">VehicleID</th>
                  <th scope="col">Roll</th>
                  <th scope="col">Pitch</th>
                  <th scope="col">Impact</th>
                  <th scope="col">Fire</th>
                  <th scope="col">Time Of Accident</th>
                  <th scope="col">Lat</th>
                  <th scope="col">Lon</th>
                  <th scope="col">Severity</th>
                  <th scope="col">Nearest Hospital</th>
                  <th scope="col">Nearest PoliceStation</th>
                  <th scope="col">Nearest FireStation</th>
                  <th scope="col">Nearest Ambulance</th>
                  <th scope="col">Current Status</th>

                </tr>
              </thead>
              <tbody>
                <?php
                  require 'DBAcess/severitycheck.php';
                  $sensor = new severitycheck;
                  $call = $sensor->getSeverityNode();
                  $c = count($call) - 1;
                  while($c>=0)
                  {
                ?>

                  <tr>
                      <td>
                        <?php 
                          $vID = array_column($call, 'vehicleID');
                          echo $vID[$c]; 
                        ?> 
                      </td>
                      <td>
                        <?php 
                            $roll = array_column($call, 'roll');
                            echo $roll[$c]; 
                        ?>
                           
                      </td>
                      <td>
                        <?php 
                          $pitch = array_column($call, 'pitch');
                          echo $pitch[$c]; 
                        ?>
                        </td>
                      <td>
                        <?php 
                          $Impact = array_column($call, 'forceSensor');
                          echo $Impact[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $fire = array_column($call, 'fire');
                          echo $fire[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $Impact = array_column($call, 'timeOfAccident');
                          echo $Impact[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $lat = array_column($call, 'lat');
                          echo $lat[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $lon = array_column($call, 'lon');
                          echo $lon[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $sev = array_column($call, 'severity');
                          echo $sev[$c];
                        ?>
                      </td>
                      <td>
                        <?php 
                          $nea = array_column($call, 'nearest_hospital');
                          echo $nea[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $pol = array_column($call, 'nearest_police');
                          echo $pol[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $fire = array_column($call, 'nearest_fire');
                          echo $fire[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $amb = array_column($call, 'nearest_amb');
                          echo $amb[$c]; 
                        ?>
                      </td>
                      <td>
                        <?php 
                          $cur = array_column($call, 'curr_status');
                          echo $cur[$c]; 
                        ?>
                      </td>



                    </tr>
                <?php 
                  $c=$c-1;   
                  }
                ?>


              </tbody>
            </table>

          </br></br></br></br>
            <form method="post"> 
                <input type="submit" name="button1"
                class="btn btn-dark" value="Find Severity" onclick="setFocusMap()" /> 
                <input type="submit" name="button2"
                class="btn btn-dark" value="Find Nearest Hospital" onclick = "setFocusMap()"/> 
                <input type="submit" name="button3"
                class="btn btn-dark" value="Find Nearest PoliceStation" onclick = "setFocusMap()"/> 
                <input type="submit" name="button4"
                class="btn btn-dark" value="Find Nearest FireStation" onclick = "setFocusMap()"/>
                <input type="submit" name="button5"
                class="btn btn-dark" value="Find Nearest Ambulance" onclick = "setFocusMap()"/> 
                <input type="submit" name="button6"
                class="btn btn-dark" value="Send Alert" onclick = "setFocus()"/>
                <button onClick="window.location.reload();" class="btn btn-dark" >Refresh Page</button>
    
            </form> 

            
            <?php
              if(array_key_exists('button1', $_POST)){
                shell_exec("python ml.py");
              }
              if(array_key_exists('button2', $_POST)){
                shell_exec("python hospital.py");   
              }
              if(array_key_exists('button3', $_POST)){
                shell_exec("python policestation.py");   
              }
              if(array_key_exists('button4', $_POST)){
                shell_exec("python firestation.py");   
              }
              if(array_key_exists('button5', $_POST)){
                shell_exec("python ambulance.py");   
              }
              if(array_key_exists('button6', $_POST)){
                shell_exec("python sendalert.py");   
              }
            ?>
            

          </div>
          </div>
      </section>

      <div id= "map_interface" class="section-title">
      <h2>Map Interface</h2>
      </br></br>
      <?php
      require 'DBAcess/activenode.php';
      $sensor = new activenode;
      $temp = $sensor->getActiveNode();
      $call = json_encode($temp, true);
      echo '<div id="data">' .$call. '</div>';

      require 'DBAcess/hospital.php';
      $h = new hospital;
      $hd = $h->getAllHospitals();
      $hdata = json_encode($hd, true);
      echo '<div id="Hos_data">' .$hdata. '</div>';

      require 'DBAcess/policestation.php';
      $p = new policestation;
      $pd = $p->getAllPolicestations();
      $pdata = json_encode($pd, true);
      echo '<div id="Pol_data">' .$pdata. '</div>';

      require 'DBAcess/firestation.php';
      $f = new firestation;
      $fd = $f->getAllFireStations();
      $fidata = json_encode($fd, true);
      echo '<div id="Fir_data">' .$fidata. '</div>';

      require 'DBAcess/ambulance.php';
      $A = new ambulance;
      $Ad = $A->getAllAmbulances();
      $Adata = json_encode($Ad, true);
      echo '<div id="Amb_data">' .$Adata. '</div>';

      ?>
      <div id="map" class="map"><div id="popup" class="ol-popup">
        <a href="#" id="popup-closer" class="ol-popup-closer"></a>
      <div id="popup-content"></div>
    </div></div>
    </div>  
    </br></br>




    </main>

    
    
    
 

    <!-- Footer -->
    <footer class="page-footer font-small blue">

      <!-- Copyright -->
      <div class="footer-copyright text-center py-3">© 2020 Copyright:
        <a href="https://mdbootstrap.com/"> aathiktr@gmail.com</a>
      </div>
      <!-- Copyright -->

    </footer>
    <!-- Footer -->
    <a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

    <!-- Vendor JS Files -->
    <script src="assets/vendor/jquery/jquery.min.js"></script>
    <script src="assets/vendor/jquery.easing/jquery.easing.min.js"></script>
 
    <!-- Template Main JS File -->
    <script src="assets/js/main.js"></script>

    <script type="text/javascript" src="./js/map.js" ></script>


  </body>
</html>