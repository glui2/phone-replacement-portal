<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Click Proceed and place a request for a replacement handset using the order form.">
                <b-button to="/orderreplacement">Proceed</b-button>
            </b-form-group>
        </b-row>
    </div>  
</template>
<script>
export default {
    data() {
        return {
            buttonClicked: '',
            proceed: [
                { text: 'Proceed', value: 'Yes'}
            ]
        }
    },
    
}
</script>
<style scoped>
.triage-radio-question { 
    color: white;     
    justify-content: center;
    margin: 3%;
}
</style>