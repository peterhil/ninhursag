<script>
    import DataLoader from '../components/DataLoader.svelte'
    import References from '../components/References.svelte'
    import SvgChart from '../components/SvgChart.svelte'
    import Images from '../components/Images.svelte'
    import CheckboxShowAll from '../components/CheckboxShowAll.svelte'
    import LogScaleCheckbox from '../components/LogScaleCheckbox.svelte'
    import SelectFunction from '../components/SelectFunction.svelte'
    import SelectMineral from '../components/SelectMineral.svelte'

    import { chart } from '../stores/chart'
    import { fn } from '../stores/function'
    import { scale } from '../stores/scale'
    import { showAll } from '../stores/showAll'
    import { mineral } from '../stores/mineral'

    const caption = 'U.S. Geological Survey statistics (Metric tons gross weight)'
</script>

<div class="row">
    <div class="small-12 large-9 columns">
        <h2>{$mineral}</h2>

        <section class="controls">
            <div class="selections">
                <SelectMineral bind:selected="{$mineral}" />
                <SelectFunction bind:selected="{$fn}" />
            </div>

            <div class="scale">
                <LogScaleCheckbox bind:scale="{$scale}" />
                {#if $scale === 'linear' }
                    <CheckboxShowAll bind:showAll="{$showAll}" />
                {/if}
            </div>
        </section>

        <figure>
            <figcaption>{caption}</figcaption>
            <DataLoader let:data data="{chart}">
                <SvgChart {data}></SvgChart>
            </DataLoader>
        </figure>
    </div>

    <aside class="small-12 large-3 columns">
        <Images mineral={$mineral} />
        <References />
    </aside>
</div>
