<?php

namespace App\Http\Controllers;
use App\State;
use Illuminate\Support\Facades\Storage;
use Illuminate\Http\Request;

class StateController extends Controller
{
    public function Index()
    {
      $states = State::all();
      $test = Storage::get('public/states/summary/Alabama.txt');

      return view('states.index', compact('states','test'));
    }
}
