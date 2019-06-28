addpath( genpath( '../Tools' ) );

dataset = 'topic_6000';
data_dir = fullfile( '..', 'Sandbox', 'Data', dataset );
results_dir = fullfile( '..', 'Sandbox', 'Results', dataset );
model_dir = fullfile( '..', 'Sandbox', 'Results', dataset, 'model' );

trn_lbl_mat = read_text_mat( fullfile( data_dir, 'trn_X_Y.txt' ) );

wts = inv_propensity( trn_lbl_mat, 0.55, 1.5 );
fid = fopen(fullfile( data_dir, 'inv_prop.txt' ),'w');
fprintf(fid,'%.4f\n',wts);    
fclose(fid)