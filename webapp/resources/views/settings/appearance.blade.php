<x-layouts.app :title="__('Appearance | Settings')">
<div class="flex flex-col items-start">
    @include('partials.settings-heading')

    <x-settings.layout :heading="__('Appearance')" :subheading=" __('Update the appearance settings for your account')">
        <fieldset>
            <legend class="sr-only">Appearance</legend>
            <x-button.group>
                <x-button type="button" variant="secondary" before="phosphor-sun-fill" value="light" onclick="setAppearance(this.value)">{{ __('Light') }}</x-button>
                <x-button type="button" variant="secondary" before="phosphor-moon-fill" value="dark" onclick="setAppearance(this.value)">{{ __('Dark') }}</x-button>
                <x-button type="button" variant="secondary" before="phosphor-monitor-fill" value="system" onclick="setAppearance(this.value)">{{ __('System') }}</x-button>
            </x-button.group>
        </fieldset>
    </x-settings.layout>
</div>
</x-layouts.app>
