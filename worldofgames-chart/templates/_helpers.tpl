{{/*
Expand the name of the chart.
*/}}
{{- define "worldofgames-chart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Expand the full name of the chart.
*/}}
{{- define "worldofgames-chart.fullname" -}}
{{- $name := default .Values.nameOverride .Chart.Name -}}
{{- printf "%s-%s" $name .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create chart labels
*/}}
{{- define "worldofgames-chart.labels" -}}
helm.sh/chart: {{ include "worldofgames-chart.chart" . }}
{{ include "worldofgames-chart.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "worldofgames-chart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "worldofgames-chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/*
Expand the chart name
*/}}
{{- define "worldofgames-chart.chart" -}}
{{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
{{- end -}}
