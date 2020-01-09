<template>
    <b-container>
        <h1 class="headings">Order a Replacement Part</h1>
        <h4 class="headings">Please complete the following details:</h4>
        <b-modal ref="orderReplacementPartModal" id="orderReplacementPartModal" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>A request for a replacement will be raised with the following details: </p>
                <div class="my-4">
                    <b-row class="my-2" v-for="(value, input) in handsetForm" :key="input">
                        <b-col sm="3">
                            <label class="modal-label" :for="`input-${input}`">{{ value.label }}:</label>
                        </b-col>
                        <b-col sm="9">
                            <p class="modal-value" :id="`input-${input}`">{{ value.value }}</p>
                        </b-col>
                    </b-row>
                </div>
                <p class="mt-4"> If the above details are correct, please press the <strong>Submit</strong> button below and a team member from the CAT team will arrange your replacement as soon as possible.</p> 
            </div> 
            <b-row>
                    <b-button class="my-5 mx-auto modal-cancel-button" block @click="hideModal('orderReplacementPartModal')"> Cancel </b-button>
                    <b-button class="my-5 mx-auto modal-submit-button" block @click="submitRequest"> Submit </b-button>
            </b-row>
        </b-modal>
        <div class="d-block">
            <b-form @submit="onSubmit" novalidate>
                <p class="error-message" v-if="notif.length">
                    <b>Notification:</b>
                    <ul>
                        <li v-for="(error, index) in notif" :key="`error-${index}`">{{ error }}</li>
                    </ul>
                </p>
                <b-form-group id="group-siteid">
                    <b-row>
                        <b-col sm="3">
                            <label class="label" for="site-id">{{ handsetForm.siteID.label }}:</label>
                        </b-col>
                        <b-col sm="9">
                            <b-form-input id="site-id" v-model="handsetForm.siteID.value" required placeholder="eg. S123456"></b-form-input>
                        </b-col>
                    </b-row>
                </b-form-group>
                <b-form-group id="group-handset-model">
                     <b-row>
                        <b-col sm="3">
                            <label class="label" for="handset-model">{{ handsetForm.handsetModel.label }}</label>
                        </b-col>
                        <b-col sm="9">                            
                            <b-form-input id="handset-model" v-model="handsetForm.handsetModel.value" required placeholder="eg. Mitel 3300"></b-form-input>
                        </b-col>
                     </b-row>
                </b-form-group>
                <b-form-group id="group-part-number">
                    <b-row>
                        <b-col sm="3">
                            <label class="label" for="part-number">{{ handsetForm.partNumber.label }}</label>
                        </b-col>
                        <!-- <b-col v-if="partNumberProp" sm="9">
                            <b-form-input id="part-number" :value="partNumberProp" placeholder=""></b-form-input>
                        </b-col>
                        <b-col v-else sm="9">
                            <b-form-input id="part-number" :value="partNumberProp.default" placeholder=""></b-form-input>
                        </b-col> -->
                        <b-col sm="9">
                            <b-form-input id="fault-description" v-model="handsetForm.partNumber.value" required placeholder=""></b-form-input>
                        </b-col>
                    </b-row>
                </b-form-group>
                <b-form-group id="group-fault-description">
                    <b-row>
                        <b-col sm="3">
                            <label class="label" for="fault-description">{{ handsetForm.faultDescription.label }}</label>
                        </b-col>
                        <b-col sm="9">
                            <b-form-input id="fault-description" v-model="handsetForm.faultDescription.value" required placeholder=""></b-form-input>
                        </b-col>
                    </b-row>
                </b-form-group>
                <b-form-group id="group-quantity">
                    <b-row>
                        <b-col sm="3">
                            <label class="label" for="quantity">{{ handsetForm.quantity.label }}</label>
                        </b-col>
                        <b-col sm="9">
                            <b-form-input id="quantity" v-model="handsetForm.quantity.value" required placeholder="eg. 2"></b-form-input>
                        </b-col>
                    </b-row>
                </b-form-group>
                <b-form-group id="group-contact-name">
                    <b-row>
                        <b-col sm="3">
                            <label class="label" for="contact-name">{{ handsetForm.contactName.label }}</label>
                        </b-col>
                        <b-col sm="9">
                            <b-form-input id="contact-name" v-model="handsetForm.contactName.value" required placeholder="eg. John Smith"></b-form-input>
                        </b-col>
                    </b-row>
                </b-form-group>
                <b-form-group id="group-contact-number">
                    <b-row>
                        <b-col sm="3">
                            <label class="label" for="contact-number">{{ handsetForm.contactNumber.label }}</label>
                        </b-col>
                        <b-col sm="9">
                            <b-form-input id="contact-number" v-model="handsetForm.contactNumber.value" required placeholder="eg. 0412345678"></b-form-input>
                        </b-col>
                    </b-row>
                </b-form-group>
                <b-form-group id="group-contact-email">
                    <b-row>
                        <b-col sm="3">
                            <label class="label" for="contact-email">{{ handsetForm.contactEmail.label }}</label>
                        </b-col>
                        <b-col sm="9">
                            <b-form-input id="contact-email" v-model="handsetForm.contactEmail.value" required placeholder="eg. john.smith@gmail.com"></b-form-input>
                        </b-col>
                    </b-row>
                </b-form-group>
                <b-form-group id="group-delivery-address">
                    <b-row>
                        <b-col sm="3">
                            <label class="label" for="delivery-address">{{ handsetForm.deliveryAddress.label }}</label>
                        </b-col>
                        <b-col sm="9">
                            <b-form-input id="delivery-address" v-model="handsetForm.deliveryAddress.value" required placeholder="eg. 123 Fake Street, Melbourne"></b-form-input>
                        </b-col>
                    </b-row>
                </b-form-group>
                <div class="nav-buttons">
                    <b-btn class="btn back-button" @click="$router.go(-1)">Back</b-btn>
                    <b-btn class="btn proceed-button" type="submit">Request</b-btn>
                    <!-- <b-btn v-b-modal.orderReplacementPartModal class="btn proceed-button">Request</b-btn> -->
                </div> 
            </b-form>
        </div>      
    </b-container>
</template>
<script>
import axios from "axios";

export default {
    data() {
        return {
            handsetForm: {
                siteID: {
                    label: "Site ID",
                    value: ''
                },
                handsetModel: {
                    label: "Handset Model",
                    value: ''
                },
                partNumber: {
                    label: "Part Number",
                    value: ''
                },
                faultDescription: {
                    label: "Fault Description",
                    value: ''
                },
                quantity: {
                    label: "Quantity",
                    value: ''
                },
                contactName: {
                    label: "Contact Name",
                    value: ''
                },
                contactNumber: {
                    label: "Contact Number",
                    value: ''
                },
                contactEmail: {
                    label: "Contact Email",
                    value: ''
                },
                deliveryAddress: {
                    label: "Delivery Address",
                    value: ''
                }
            },
            notif: [],
        }
    },
    props: {
      partNumberProp: {
          type: String,
          default: ''
      }
    },
    computed: {
        hasPartNumberProp() {
            if(this.partNumberProp){
                return this.handsetForm.partNumber.value = this.partNumberProp; 
            }
        }
    },
    methods: {
        onSubmit(evt) {
            evt.preventDefault();            
            this.notif = []; 
            if(!this.handsetForm.siteID.value){
                this.notif.push("Please enter your Site ID.");
            }

            if(!this.handsetForm.handsetModel.value){
                this.notif.push("Please specify your handset model.");
            }

            if(!this.handsetForm.faultDescription.value){
                this.notif.push("Please describe the problem with your device.");
            }

            if(!this.handsetForm.quantity.value){
                this.notif.push("Please tell us how many units you would like to order.");
            }

            if(!this.handsetForm.contactName.value){
                this.notif.push("Please provide the name of someone to contact.");
            }

            if(!this.handsetForm.contactNumber.value){
                this.notif.push("Please provide a contact number for the person specified.");
            }

            if(!this.handsetForm.deliveryAddress.value){
                this.notif.push("Please provide an address to deliver your replacement handsets to.");
            }

            if (!this.notif.length){
                this.showModal('orderReplacementPartModal');
                return true;
            }
        },
        showModal(modalRef) {
            this.$refs[modalRef].show(); 
        },
        hideModal(modalRef) {
            this.$refs[modalRef].hide();
        },
        testRequest() { 
            const path = 'http://127.0.0.1:5000/api/requesthandsetreplacement'
            axios.get(path)
                .then((result) => {
                        this.notif.push(result.data);
                    }
                )
                .catch((error) => {
                    console.error(error)
                })
        },
        submitRequest() {
            const path = 'http://127.0.0.1:5000/api/requesthandsetreplacement'
            const payload = {
                siteID: this.handsetForm.siteID.value,
                handsetModel: this.handsetForm.handsetModel.value,
                partNumber: this.handsetForm.partNumber.value,
                faultDescription: this.handsetForm.faultDescription.value,
                quantity: this.handsetForm.quantity.value,
                contactName: this.handsetForm.contactName.value,
                contactNumber: this.handsetForm.contactNumber.value,
                contactEmail: this.handsetForm.contactEmail.value,
                deliveryAddress: this.handsetForm.deliveryAddress.value,
            }

            axios
                .post(path, payload)
                .then((response) => {
                    this.notif.push(response.data)
                    console.log('Server response: ' + response);
                })
                .catch((error) => {
                    this.notif.push(response.data)
                    console.log('Server error: ' + error);
                });
            this.hideModal('orderReplacementPartModal');
        }
    },      
    
}
</script>
<style scoped>
.btn.back-button {
    color: #A0FFF5;
    background: none;
    border: none;
    bottom: 10%; 
}

.btn.proceed-button {
    color: #A0FFF5;
    background: none;
    border: none;
    bottom: 10%; 
    right: 0px;
}

.btn.back-button:hover, .btn.proceed-button:hover {
    color: #A0FFF5; 
    background-color: #FFFFFF40;
    border: none;  
}

.btn.back-button:active, .btn.proceed-button:active {
    color: #A0FFF5; 
    background-color: #FFFFFF10;
    border: none; 
}

.btn.back-button:focus, .btn.proceed-button:focus {
    border: none; 
}

.error-message {
    color: #A0FFF5; 
    margin: 5%;
}

.form {
    justify-items: center; 
}

.headings {
    color: white; 
    text-align: center;
    margin: 5%;
}

.label {
    color: white;
    font-weight: bold;
}

.modal-label {
    color: black;
    font-weight: bold; 
}

.nav-buttons {
    text-align: center; 
    margin: 3%;
}

#orderReplacementPartModal .modal-body-text {
    text-align: left;
}

#orderReplacementPartModal .modal-cancel-button {
    background-color: #B5B5B5;
    border: none;
    width: 33%; 
}

#orderReplacementPartModal .modal-submit-button {
    background-color: #576DC3;
    border: none;
    width: 33%;
}

</style>