<template>
    <b-container>
        <p class="tech-instructions" v-if="howto"><strong>Please progress through the following steps.</strong></p>
        <p v-if="howto=='MITEL330053H1'" class="tech-instructions">
            <ol>
                <li>Unplug the network cable from the back of the phone or from the wall socket. </li>
                <li>Press down on both the UP and DOWN arrow buttons and keep them pressed. </li>
                <li>Plug the Ethernet cable to the phone. </li>
                <li>Release only the DOWN arrow key, keeping the UP arrow key pressed down. </li>
                <li>Wait until “Configure Phone” appears on the screen, then you can release the UP arrow key. </li>
                <li>At the “Configure Phone” option, press * for YES. </li>
                <li>At the “Network Parameters” option, press * for YES. </li>
                <li>At the “View Current parameters” option, press # for NO. </li>
                <li>At the “Static QOS” option, press * for YES. </li>
                <li>At the “View QOS Parameters” option, press # for NO. </li>
                <li>At the “Modify QOS Parameters” option, press * for YES. </li> 
                <li>At this stage use the arrow down button and scroll down once. </li>
                <li>At “VLAN ID”, use the phone keypad to enter the VLAN ID you are using for the Voice Network (this can be obtained from your IT) </li>
                <li>After entering the VLAN ID there is no additional input required, so keep scrolling down until you reach the “STORE CHANGES” option. </li>
                <li>At the “STORE CHANGES” option press * for YES.  The phone will save the new configuration to the NVRAM. </li>
                <li>When prompted to “REBOOT NOW”, press * for YES. </li>
                </ol>
            The phone will reset and will start up with the new configuration and should show the time and date on the screen to indicate a proper registration.       
        </p>
        <p v-if="howto=='MITEL330053H2'" class="tech-instructions">
            <ol>
                <li>Unplug the network cable from the back of the phone or from the wall socket. </li>
                <li>Press down on both the UP and DOWN arrow buttons and keep them pressed. </li>
                <li>Plug the Ethernet cable to the phone. </li>
                <li>Release only the DOWN arrow key, keeping the UP arrow key pressed down. </li>
                <li>Wait until “Configure Phone” appears on the screen, then you can release the UP arrow key. </li>
                <li>At the “Configure Phone” option, press * for YES. </li>
                <li>At the “Network Parameters” option, press * for YES. </li>
                <li>At the “View Current parameters” option, press # for NO. </li>
                <li>At the “Static QOS” option, press # for NO. </li>
                <li>At the “Static IPV4" option, press * for YES. </li>
                <li>At the “View IPV4 Params” option, press # for NO. </li>
                <li>At the “Modify IPV4 Params” option, press * for YES. </li>
                <li>Using the Down arrow key, scroll down once and enter the following information: </li>
            <ul>
                <li>Enter the phone IP address (given to you by your IT team).</li>
                <li>For example, if the IP address is 10.20.134.80, then using the keypad on the phone, enter 010.020.134.080 or you can enter the IP address by pressing 10#20#134#80#.  Then press the Down arrow key once.</li>
                <li>Enter the Default Gateway IP address (given to you by your IT team) then press the Down arrow key once.</li>
                <li>Enter the Subnet Mask (given to you by your IT team), then press the Down arrow key once.</li>
                <li>Enter the ICP IP address, this is the PABX (MiVoice Business Controller) IP address (given to you by your IT team), then press the down arrow key once.</li>
                <li>Enter the TFTP SVR IP address (this IP address in most cases can be the same as the IP address given to you in step 5), then press the Down arrow key once.</li>
                <li>There is no requirement to fill in any of the rest of the option afterwards, so keep scrolling down until you get to “STORE CHANGES” and press * for YES.</li>
                <li>Reboot the phone when prompted.</li>
            </ul>
            The phone will reset and will start up with the new configuration and should show the time and date on the screen to indicate a proper registration.
            </ol>
        </p>
        <p v-if="howto=='MITEL330053H3'" class="tech-instructions">
            <ol>
                <li>Unplug the network cable from the back of the phone or from the wall socket. </li>
                <li>Press down on both the UP and DOWN arrow buttons and keep them pressed. </li>
                <li>Plug the Ethernet cable to the phone. </li>
                <li>Release only the DOWN arrow key, keeping the UP arrow key pressed down. </li>
                <li>Wait until “Configure Phone” appears on the screen, then you can release the UP arrow key. </li>
                <li>At the “Configure Phone” option, press * for YES. </li>
                <li>At the “Network Parameters” option, press # for NO. </li>
                <li>At the “H/W Config” option, press # for NO. </li>
                <li>At the “Phone Mode” option, press # for NO. </li>
                <li>At the “Tools and features” option, press # for NO. </li>
                <li>At the “View Version Information” option, press * for YES. </li>
                <li>At the “Current version Info” option, scroll down to find the information needed. As an example you will see something that resembles the below:</li>
                    <table class="example-table">
                        <tr>
                            <td><strong>Main Load Version</strong></td>
                            <td>06.05.00.11</td>
                        </tr>
                        <tr>
                            <td><strong>Boot Load Version</strong></td>
                            <td>06.04.01.02</td>
                        </tr>
                        <tr>
                            <td><strong>L2Boot Load Version</strong></td>
                            <td>06.01.00.10</td>
                        </tr>
                        <tr>
                            <td><strong>DSP Load Version</strong></td>
                            <td>3.0.0.21</td>
                        </tr>
                    </table>
                <li>You can exit menu by pressing the exit option at any time.</li>
            </ol>
        </p>
        <p v-if="howto=='MITEL330053H4'" class="tech-instructions">
            <ol>
                <li>Unplug the network cable from the back of the phone or from the wall socket. </li>
                <li>Press down on both the UP and DOWN arrow buttons with your thumb and keep them pressed. </li>
                <li>Plug the Ethernet cable to the phone. </li> 
                <li>Release only the DOWN arrow key, keeping the UP arrow key pressed down. </li>
                <li>Wait until “Configure Phone” appears on the screen, then you can release the UP arrow key. </li>
                <li>At the “Configure Phone” option press * for YES. </li>
                <li>At the “Network Parameters” option press # for NO. </li>
                <li>At the “H/W Config” option press # for NO. </li>
                <li>At the “Phone Mode” option press # for NO. </li>
                <li>At the “Tools and features” option press * for YES. </li>
                <li>At the “Erase PIN” option, press # for NO. </li>
                <li>At the “Edit 802/x Setting” option, press # for NO. </li>
                <li>At the “Edit CDP Setting” option, press # for NO. </li>
                <li>At the “Edit LLDP Setting” option, press # for NO. </li>
                <li>At the “Edit GIGE Setting” option, press # for NO (this option may not be present for all models, so if you do not see it just ignore it). </li>
                <li>At the “Ping Test” option, press # for NO. </li>
                <li>At the “DHCP Trace” option, press # for NO. </li>
                <li>At the “Port Options” option, press # for NO. </li>
                <li>At the “Disable Packet Filter” option, press # for NO. </li>
                <li>At the “Diagnostics” option, press # for NO. </li>
                <li>At the “Restore Defaults” option, Press * for YES. </li>
                <li>At the “Confirm” option, Press * for YES. </li>
                <li>The phone will reboot with the factory default settings. </li>
            </ol>
        </p>
        <p v-if="howto=='MITEL330053H5'" class="tech-instructions">
            Please note this procedure only applies to replacing a faulty handset with one of the exact same model (you can confirm by checking that the part numbers listed on the white sticker on the back of both phones match). <br/><br/>
            Using the handset replacement feature code (by default it is ###), you can find this code by browsing to the controller (PABX) and access the following menu option:
            System Options / replacement access code

            The procedure is as follows:
            <ol>
                <li>Once the replacement handset is plugged in and powered up (give it 30 sec to 45 sec for the handset to reboot), the screen will display Enter your pin, then you can enter ### Extension number then press on the hold key.  For example if the extension is 300, then you use the keypad to enter (depending on the model of the handset)</li>
                <li>### 300 press on the Blue button or ### 300 press on the red button</li>
                <li>At this stage the display on the handset should display the normal date and time which indicates that the handset has been successfully registered.</li>
                <li>Make outgoing / incoming calls to confirm that the handset is in a working order. </li>
            </ol>
        </p>
        <p v-if="howto=='MITEL330069H1'" class="tech-instructions">
            <ol>
                <li>Once the handset boots up, press on the <strong>settings</strong> button (the second button from the bottom) on the left hand side.</li>
                <li>On the screen display select “Advanced” button.</li>
                <li>Enter the “admin” password.  By default the admin password is 73738. Then press enter.</li>
                <li>Press the right arrow key or swipe the screen (for Mitel 6940 models) and select “Network” from the menu.</li>
                <li>Using the navigation keys scroll up or down to select the “VLAN" Icon, then apply the following configuration below. You can use the down arrow key to move from one option to the next.</li>
            </ol>
            <table class="example-table">
                <tr>
                    <td><strong>VLAN</strong></td>
                    <td>7</td>
                </tr>
                <tr>
                    <td><strong>L2P Default</strong></td>
                    <td>No Change</td>
                </tr>
                <tr>
                    <td><strong>L2P Voice</strong></td>
                    <td>No Change</td>
                </tr>
                <tr>
                    <td><strong>L2P Signalling</strong></td>
                    <td>No Change</td>
                </tr>
                <tr>
                    <td><strong>L2P Other</strong></td>
                    <td>No Change</td>
                </tr>
                <tr>
                    <td><strong>DSCP Default</strong></td>
                    <td>No Change</td>
                </tr>
                <tr>
                    <td><strong>DSCP Voice</strong></td>
                    <td>No Change</td>
                </tr>
                <tr>
                    <td><strong>DSCP Signalling</strong></td>
                    <td>No Change</td>
                </tr>
                <tr>
                    <td><strong>DSCP Other</strong></td>
                    <td>No Change</td>
                </tr>
            </table>
            Then save your changes.
        </p>  
        <p v-if="howto=='MITEL330069H2'" class="tech-instructions">
            <ol>
                <li>Once the handset boots up, press on the <strong>settings</strong> button (the second button from the bottom) on the left hand side.</li>
                <li>On the screen display select “Advanced” button.</li>
                <li>Enter the “Admin” password.  By default the admin password is 73738. Then press Enter.</li>
                <li>Press the right navigation arrow key or swipe the screen (for Mitel 6940 models) and look for and select “Network”, then you can enter the following information. See example below:</li>
                <li>You can use the down arrow key to move from one option to the next.</li>

            </ol>
            <table class="example-table">
                <tr>
                    <td><strong>IP Address</strong></td>
                    <td>Phone static IP address provided by your IT</td>
                </tr>
                <tr>
                    <td><strong>Subnet Mask</strong></td>
                    <td>Network Subnet address provided by your IT</td>
                </tr>
                <tr>
                    <td><strong>Gateway Address</strong></td>
                    <td>Provided by your IT</td>
                </tr>
                <tr>
                    <td><strong>Primary DNS</strong></td>
                    <td>Normally Blank</td>
                </tr>
                <tr>
                    <td><strong>Secondary DNS</strong></td>
                    <td>Normally Blank</td>
                </tr>
                <tr>
                    <td><strong>Call Server IP Address</strong></td>
                    <td>IP Address for the phone system</td>
                </tr>
                <tr>
                    <td><strong>TFTP Server IP address</strong></td>
                    <td>IP Address for the phone system</td>
                </tr>
                <tr>
                    <td><strong>TFTP Server Port</strong></td>
                    <td>Normally Blank</td>
                </tr>
                <tr>
                    <td><strong>File Server</strong></td>
                    <td>Normally Blank</td>
                </tr>
                <tr>
                    <td><strong>IPA IP Address</strong></td>
                    <td>Normally Blank</td>
                </tr>	
            </table>
            Press Save to save changes.
        </p>
        <p v-if="howto=='MITEL330069H3'" class="tech-instructions">
            <ol>
                <li>Once the handset boots up, press on the <strong>settings</strong> button (the second button from the bottom) on the left hand side.</li>
                <li>Select the STATUS option by using the navigation buttons.</li>
                <li>Scroll down to the Phone Info option. You will see the following information displayed.  See example below:</li>
            </ol>
            <table class="example-table">
                <tr>
                    <td><strong>Main Version</strong></td>
                    <td>01.03.00.112</td>
                </tr>
                <tr>
                    <td><strong>Call Server Rev</strong></td>
                    <td>default</td>
                </tr>
                <tr>
                    <td><strong>PKM Version</strong></td>
                    <td>Only if PKM is connected</td>
                </tr>
                <tr>
                    <td><strong>Model</strong></td>
                    <td>Minet_69xx Rev:000</td>
                </tr>
                <tr>
                    <td><strong>Phone Uptime</strong></td>
                    <td>Only for 6940 Models</td>
                </tr>
            </table>
        </p>
        <p v-if="howto=='MITEL330069H4'" class="tech-instructions">
           <ol>
                <li>Once the handset boots up, press on the <strong>settings</strong> button (the second button from the bottom) on the left hand side.</li>
                <li>On the screen display select “Advanced”.</li>
                <li>Enter the “admin” password. By default the admin password is 73738. Then press Enter.</li>
                <li>Press the right arrow key or swipe the screen (for Mitel 6940 models) and look for the menu and select “Restore default”.</li>
                <li>Select YES to confirm and restart the handset.</li>
            </ol> 
        </p>
              
    </b-container>
</template>
<script>
export default {
    props: {
        howto: String
    }
    
}
</script>
<style scoped>
.tech-instructions {
    text-align: left;
    font-size: 15px;
    color: white;
    align-self: center; 
}

.example-table {
    border-collapse: separate;
    border-spacing: 5px;
    margin: auto; 
}
</style>
