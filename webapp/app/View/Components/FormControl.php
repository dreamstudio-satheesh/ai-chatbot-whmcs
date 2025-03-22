<?php

namespace App\View\Components;

use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\View;
use Illuminate\Support\ViewErrorBag;
use Illuminate\View\Component;

abstract class FormControl extends Component
{
    public $id;

    public $value;

    public $label;

    public $formControlAttributes;

    public function __construct($name, $id = null, $value = '', $label = '', $bag = 'default')
    {
        $sessionPath = self::sessionPath($name);
        $this->value = old($sessionPath, $value);
        $this->label = $label;
        $this->id = $id ?? $name;
        $this->formControlAttributes = $this->newAttributeBag([
            'name' => $name,
            'id' => $this->id,
        ])->when($this->errorBag($bag)->has($sessionPath), function ($attributes) use ($name) {
            $attributes->offsetSet('aria-invalid', 'true');
            $attributes->offsetSet('aria-describedby', $attributes->prepends($name.'_error'));
        });
    }

    protected function errorBag($name = 'default')
    {
        $bags = View::shared('errors', fn () => Session::get('errors', new ViewErrorBag));

        return $bags->getBag($name);
    }

    public static function sessionPath($name)
    {
        return trim(str_replace(['[', ']'], ['.', ''], $name), '.');
    }
}
