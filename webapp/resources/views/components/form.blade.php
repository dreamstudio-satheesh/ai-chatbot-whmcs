@props(['method' => 'get', 'action' => '', 'upload' => false])

<form method="{{ $method !== 'get' ? 'post' : 'get' }}" action="{{ $action }}" {{ $attributes->merge(['enctype' => $upload ? 'multipart/form-data' : null]) }}>
    <input hidden type="hidden" name="_token" value="{{ csrf_token() }}" autocomplete="off">
    <input hidden type="hidden" name="_method" value="{{ $method }}">
    {{ $slot }}
</form>
