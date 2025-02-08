#version 330 core

layout (location = 0) out vec4 fragColor;

in vec4 fragPosition;

uniform vec3 cameraPosition;


void main() {
    // Output fragment color
    float depth = length(cameraPosition - fragPosition.xyz);
    if (depth < 4) 
        discard;
        //fragColor = vec4(1.0, 0.0, 0.0, 1.0);
    else
        fragColor = vec4(1.0, 1.0, 1.0, 1.0);
}