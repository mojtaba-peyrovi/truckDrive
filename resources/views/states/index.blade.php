<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <ul>
      @foreach ($states as $state)
          <li>{{ $state->title}}</li>
          <li>{{ $state->summary}}</li>
      @endforeach


        {{$test}}



    </ul>
  </body>
</html>
